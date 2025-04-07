package com.example.lab3.controller;

import com.example.lab3.utils.JSONUtils;
import com.example.lab3.utils.CommonSQLRequests;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;

@WebServlet("/admin")
public class AdminServlet extends HttpServlet {

    private static class Body {
        public String password;
        public int queueId;
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        var body = (Body) JSONUtils.parseBody(request, Body.class);

        if (CommonSQLRequests.isPasswordCorrect(body.queueId, body.password)) {
            var queueInfo = CommonSQLRequests.getQueueInfo(body.queueId);
            var users = CommonSQLRequests.getUsers(body.queueId);
            assert queueInfo != null;
            assert users != null;

            request.setAttribute("queueId", queueInfo.get("id"));
            request.setAttribute("queueName", queueInfo.get("name"));
            request.setAttribute("isQueueOpen", queueInfo.get("isOpen"));
            request.setAttribute("users", users);

            request.getRequestDispatcher("/admin.jsp").forward(request, response);
        } else {
            response.setStatus(HttpServletResponse.SC_UNAUTHORIZED);
        }
    }
}