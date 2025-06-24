
def get_nested_attributes(self, obj, attr_list):
    result = {}
    for attr_path in attr_list:
        try:
            parts = attr_path.split(".")
            current = obj
            for part in parts:
                try:
                    current = getattr(current, part)
                except AttributeError:
                    continue
            result[attr_path] = current
        except AttributeError:
            result[attr_path] = None  # or raise or log if needed
    return result
