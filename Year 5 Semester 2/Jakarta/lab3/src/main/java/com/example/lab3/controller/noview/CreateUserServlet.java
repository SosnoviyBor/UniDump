package com.example.lab3.controller.noview;

import com.example.lab3.utils.CommonSQLRequests;
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

@WebServlet("/create/user")
public class CreateUserServlet extends HttpServlet {

    public static class Json {
        public String name;
        public int queueId;
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        var json = (Json) JSONUtils.parseBody(request, Json.class);

        JDBCUtils.trickJdbcIntoThinking();
        try (
                var connection = DriverManager.getConnection(JDBCUtils.jdbcUrl);
                var statementInsert = connection.prepareStatement("""
                        INSERT INTO user (name, queue_id)
                        VALUES (?, ?)""");
        ) {
//            yeah, i know java, how could you tell?
            if ((boolean) Objects.requireNonNull(CommonSQLRequests.getQueueInfo(json.queueId)).get("isOpen")) {
                statementInsert.setString(1, json.name);
                statementInsert.setInt(2, json.queueId);
                statementInsert.executeUpdate();
            }
            response.setStatus(HttpServletResponse.SC_OK);
        } catch (SQLException e) {
            e.printStackTrace(System.err);
            response.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
        }
        response.setContentType("text/plain");
        response.getWriter().write("");
    }
}