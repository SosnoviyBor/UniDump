package com.example.lab3.controller;

import com.example.lab3.utils.CommonSQLRequests;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;

@WebServlet("/queue/*")
public class QueueServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        var queueId = Integer.parseInt(request.getPathInfo().substring(1));

        var queueInfo = CommonSQLRequests.getQueueInfo(queueId);
        var users = CommonSQLRequests.getUsers(queueId);
        assert queueInfo != null;
        assert users != null;

        request.setAttribute("queueId", queueInfo.get("id"));
        request.setAttribute("queueName", queueInfo.get("name"));
        request.setAttribute("isQueueOpen", queueInfo.get("isOpen"));
        request.setAttribute("users", users);

        request.getRequestDispatcher("/queue.jsp").forward(request, response);
    }
}