def slices(series, length):
    if series and length <= len(series) and length > 0:
        return [series[offset:offset+length] for offset in range(len(series)-length+1)]
    else:
        raise ValueError('Wrong input')