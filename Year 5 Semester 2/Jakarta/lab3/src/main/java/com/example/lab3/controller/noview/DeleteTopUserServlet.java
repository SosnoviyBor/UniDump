package com.example.lab3.controller.noview;

import com.example.lab3.utils.JDBCUtils;
import com.example.lab3.utils.JSONUtils;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.HashMap;

@WebServlet("/delete/user/top")
public class DeleteTopUserServlet extends HttpServlet {

    public static class Json {
        public int queueId;
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        var json = (Json) JSONUtils.parseBody(request, Json.class);

        JDBCUtils.trickJdbcIntoThinking();
        try (
                var connection = DriverManager.getConnection(JDBCUtils.jdbcUrl);
                var statement = connection.prepareStatement("""
                        DELETE FROM user
                        WHERE id = (
                            SELECT min(id)
                            FROM user
                            WHERE user.queue_id = ?
                        )""");
        ) {
            statement.setInt(1, json.queueId);
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