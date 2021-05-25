package com.example.Calculator;

import javax.servlet.http.Cookie;

public class Util {

    public String unnulifier(String parameter) {
        if (parameter == null) {
            return "";
        } else {
            return parameter;
        }
    }

    public Cookie newCookieGen (String key, String value, int age) {
        Cookie cookie = new Cookie(key, value);
        cookie.setMaxAge(age);
        return cookie;
    }

    public String getCookieVal(Cookie[] cookies, String key) {
        if(cookies !=null) {
            for(Cookie c: cookies) {
                if(key.equals(c.getName())) {
                    return c.getValue();
                }
            }
        }
        return "";
    }
}
