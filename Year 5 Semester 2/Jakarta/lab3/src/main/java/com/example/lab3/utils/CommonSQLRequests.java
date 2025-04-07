package com.example.lab3.utils;

import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.HashMap;

public class CommonSQLRequests {

    public static HashMap<Object, Object> getQueueInfo(int queueId) {
        JDBCUtils.trickJdbcIntoThinking();

        try (
                var connection = DriverManager.getConnection(JDBCUtils.jdbcUrl);
                var statement = connection.prepareStatement("""
                        SELECT id, name, is_open
                        FROM queue
                        WHERE id = ?""");
        ) {
            statement.setInt(1, queueId);
            var rs = statement.executeQuery();
            var queueInfo = new HashMap<>();
            queueInfo.put("id", rs.getInt("id"));
            queueInfo.put("name", rs.getString("name"));
            queueInfo.put("isOpen", rs.getBoolean("is_open"));
            return queueInfo;
        } catch (SQLException e) {
            e.printStackTrace(System.err);
        }
        return null;
    }

    public static ArrayList<Object> getQueueList() {
        JDBCUtils.trickJdbcIntoThinking();

        var queueList = new ArrayList<>();
        try (
                var connection = DriverManager.getConnection(JDBCUtils.jdbcUrl);
                var statement = connection.createStatement();
                var rsQueue = statement.executeQuery("""
                        SELECT id, name
                        FROM queue""");
                var statementSize = connection.prepareStatement("""
                    SELECT count(id) AS size
                    FROM user
                    WHERE queue_id = ?""")
        ) {
            while (rsQueue.next()) {
                var queueInfo = new HashMap<>();
                queueInfo.put("id", rsQueue.getInt("id"));
                queueInfo.put("name", rsQueue.getString("name"));

                statementSize.setInt(1, rsQueue.getInt("id"));
                var rsSize = statementSize.executeQuery();
                queueInfo.put("size", rsSize.getInt("size"));

                queueList.add(queueInfo);
            }
        } catch (SQLException e) {
            e.printStackTrace(System.err);
        }

        return queueList;
    }

    public static ArrayList<Object> getUsers(int queueId) {
        JDBCUtils.trickJdbcIntoThinking();

        try (
                var connection = DriverManager.getConnection(JDBCUtils.jdbcUrl);
                var statement = connection.prepareStatement("""
                        SELECT id, name
                        FROM user
                        WHERE queue_id = ?
                        ORDER BY id""");
        ) {
            statement.setInt(1, queueId);
            var rs = statement.executeQuery();
            var users = new ArrayList<>();
            while (rs.next()) {
                var user = new HashMap<>();
                user.put("id", rs.getInt("id"));
                user.put("name", rs.getString("name"));
                users.add(user);
            }
            return users;
        } catch (SQLException e) {
            e.printStackTrace(System.err);
        }
        return null;
    }

    public static boolean isPasswordCorrect(int queueId, String password) {
        JDBCUtils.trickJdbcIntoThinking();

        try (
                var connection = DriverManager.getConnection(JDBCUtils.jdbcUrl);
                var statement = connection.prepareStatement("""
                        SELECT EXISTS(
                            SELECT 1
                            FROM queue
                            WHERE password = ? AND id = ?) AS result""");
        ) {
            statement.setString(1, password);
            statement.setInt(2, queueId);
            var rs = statement.executeQuery();
            var result = rs.getInt("result");
            return switch (result) {
                case 0 -> false;
                case 1 -> true;
                default -> false;
            };
        } catch (SQLException e) {
            e.printStackTrace(System.err);
        }
        return false;
    }
}
