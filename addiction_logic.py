def detect_addiction(screen_time, social_time, app_opens, night_usage):
    score = 0

    if screen_time > 6:
        score += 2
    if social_time > 3:
        score += 2
    if app_opens > 50:
        score += 1
    if night_usage == "yes":
        score += 1

    if score >= 5:
        return "High Risk"
    elif score >= 3:
        return "Moderate Risk"
    else:
        return "Low Risk"
