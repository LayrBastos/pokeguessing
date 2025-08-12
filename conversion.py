def height(h):
    if h < 10:
        return f"{h * 10}cm"
    else:
        return f"{h / 10}m"
    

def weight(w):
    w /= 10
    return f"{round(w, 1)}kg"