from tigrbl_auth.standards.http.cookies import COOKIE_VALUE_VERSION, build_session_cookie_value, parse_session_cookie_value


def test_opaque_session_cookie_roundtrip_uses_versioned_value():
    value = build_session_cookie_value('00000000-0000-0000-0000-000000000001', 'secret')
    assert value.startswith(f"{COOKIE_VALUE_VERSION}.")
    parsed = parse_session_cookie_value(value)
    assert parsed is not None
    assert str(parsed.session_id) == '00000000-0000-0000-0000-000000000001'
    assert parsed.secret == 'secret'
