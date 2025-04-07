package com.example.lab3.utils;

import com.fasterxml.jackson.databind.ObjectMapper;
import jakarta.servlet.http.HttpServletRequest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class JSONUtils {
    public static Object parseBody(HttpServletRequest request, Class<?> jsonTemplate) throws IOException {
        // Read the JSON body from the request input stream
        StringBuilder jsonBuffer = new StringBuilder();
        String line;

        try (BufferedReader reader = new BufferedReader(new InputStreamReader(request.getInputStream()))) {
            while ((line = reader.readLine()) != null) {
                jsonBuffer.append(line);
            }
        }

        // i dont know why request encodes these symbols, but fuck me i guess
        String jsonBody = jsonBuffer.toString()
                .replace("result=", "")
                // json replacers
                .replace("%5B", "[")
                .replace("%5D", "]")
                .replace("%7B", "{")
                .replace("%7D", "}")
                .replace("%22", "\"")
                .replace("%3A", ":")
                .replace("%2C", ",")
                .replace("+",   " ")
                // other symbols
                .replace("%5C", "\\")
                .replace("%3E", ">")
                .replace("%3C", "<")
                .replace("%23", "#")
                .replace("%7C", "|")
                .replace("%3D", "=")
                .replace("%21", "!");

        // Convert the JSON string to a Java object using Jackson's ObjectMapper
        ObjectMapper objectMapper = new ObjectMapper();

        // Parse JSON into object
        return objectMapper.readValue(jsonBody, jsonTemplate);
    }
}
