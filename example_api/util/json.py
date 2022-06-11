from datetime import date, datetime, time, timezone
import json

def to_json(data, pretty_print=False):
    if pretty_print:
        return json.dumps(data, sort_keys=True, indent=2, cls=JSONEncoder)
    else:
        return json.dumps(data, separators=(',', ':'), cls=JSONEncoder)

def from_json(json_str):
    return json.loads(json_str) if json_str else None

class JSONEncoder(json.JSONEncoder):
    """Customized json encoder based on Django"""
    def default(self, obj):
        if isinstance(obj, datetime):
            # If the timezone isn't set, assume it's UTC
            if obj.tzinfo is None:
                obj = obj.replace(tzinfo=timezone.utc)

            r = obj.isoformat()

            # Reduce it down to millisecond precision
            if obj.microsecond:
                r = r[:23] + r[26:]
            if r.endswith('+00:00'):
                r = r[:-6] + 'Z'
            return r
        elif isinstance(obj, date):
            return obj.isoformat()
        elif isinstance(obj, time):
            r = obj.isoformat()

            # Reduce it down to millisecond precision
            if obj.microsecond:
                r = r[:12]
            return r
        elif hasattr(obj, 'asdict') and callable(obj.asdict):
            return obj.asdict()

        try:
            return super().default(obj)
        except TypeError:
            return str(obj)
