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
import java.util.Objects;

@WebServlet("/update/queue/status")
public class UpdateQueueStatusServlet extends HttpServlet {

    public static class Json {
        public int queueId;
        public String isOpen;
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        var json = (Json) JSONUtils.parseBody(request, Json.class);

        JDBCUtils.trickJdbcIntoThinking();
        try (
                var connection = DriverManager.getConnection(JDBCUtils.jdbcUrl);
                var statement = connection.prepareStatement("""
                        UPDATE queue
                        SET is_open = ?
                        WHERE id = ?""");
        ) {
//            0 = closed
//            1 = open
            if (Objects.equals(json.isOpen, "true")) {
                statement.setInt(1, 0);
            } else {
                statement.setInt(1, 1);
            }
            statement.setInt(2, json.queueId);
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