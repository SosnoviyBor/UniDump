package com.example.lab3.controller;

import com.example.lab3.utils.CommonSQLRequests;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;

@WebServlet("/home")
public class HomeServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        request.setAttribute("queueList", CommonSQLRequests.getQueueList());

        request.getRequestDispatcher("/home.jsp").forward(request, response);
    }
}