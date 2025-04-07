package com.example.lab3.utils;

public class JDBCUtils {
//    relative path my ass
    public static final String sqlitePath = "E:\\Data\\Homewerk\\Year 5 Semester 2\\Jakarta\\lab3\\db.db";
    public static final String jdbcUrl = "jdbc:sqlite:" + sqlitePath;

    public static void trickJdbcIntoThinking() {
//        trick jdbc into thinking it exists
        try { Class.forName("org.sqlite.JDBC"); }
        catch (ClassNotFoundException e) { throw new RuntimeException(e); }
    }
}
