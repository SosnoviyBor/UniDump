package com.example.lab3.controller.noview;

import com.example.lab3.utils.JDBCUtils;
import com.example.lab3.utils.JSONUtils;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.sql.DriverManager;
import java.sql.SQLException;

@WebServlet("/create/queue")
public class CreateQueueServlet extends HttpServlet {

    public static class Json {
        public String name;
        public String password;
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        var json = (Json) JSONUtils.parseBody(request, Json.class);

        JDBCUtils.trickJdbcIntoThinking();
        try (
                var connection = DriverManager.getConnection(JDBCUtils.jdbcUrl);
                var statement = connection.prepareStatement("""
                        INSERT INTO queue (name, password)
                        VALUES (?, ?)""");
        ) {
            statement.setString(1, json.name);
            statement.setString(2, json.password);
            statement.executeUpdate();
            response.setStatus(HttpServletResponse.SC_OK);
        } catch (SQLException e) {
            e.printStackTrace(System.err);
            response.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
        }
        response.setContentType("text/plain");
        response.getWriter().write("");
    }
}