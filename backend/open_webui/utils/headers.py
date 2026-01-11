from urllib.parse import quote


def include_user_info_headers(headers, user):
    return {
        **headers,
        "X-OptimalMD AI-User-Name": quote(user.name, safe=" "),
        "X-OptimalMD AI-User-Id": user.id,
        "X-OptimalMD AI-User-Email": user.email,
        "X-OptimalMD AI-User-Role": user.role,
    }
