# Django Security Measures

## Configured in settings.py
- `DEBUG = False` to avoid leaking sensitive errors.
- `SECURE_BROWSER_XSS_FILTER = True` to prevent XSS.
- `CSRF_COOKIE_SECURE = True` and `SESSION_COOKIE_SECURE = True` to ensure secure cookies.
- `X_FRAME_OPTIONS = 'DENY'` to protect against clickjacking.

## CSRF Protection
- All forms include `{% csrf_token %}`.

## SQL Injection Protection
- All views use Django ORM and sanitized inputs.

## CSP
- Configured via `django-csp` to allow only trusted content sources.

## Manual Tests
- Attempted form submissions without CSRF token → 403 returned.
- Searched with malicious SQL → safely handled.
- Checked browser network headers for CSP and X-Frame-Options.
