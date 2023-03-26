package task3;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.Graphics.*;

public class BounceFrame extends JFrame {
    private BallCanvas canvas;
    public static final int WIDTH = 450;
    public static final int HEIGHT = 350;
    private static final int BLUE_PRIORITY = 1;
    private static final int RED_PRIORITY = 10;

    public BounceFrame() {
        this.setSize(WIDTH, HEIGHT);
        this.setTitle("Bounce program (Task 3. Priority)");
        this.canvas = new BallCanvas();
        System.out.println("In Frame Thread name = "
                + Thread.currentThread().getName());
        Container content = this.getContentPane();
        content.add(this.canvas, BorderLayout.CENTER);
        JPanel buttonPanel = new JPanel();
        buttonPanel.setBackground(Color.lightGray);
        JButton buttonStart = new JButton("Start");
        //JButton startBlue = new JButton("Add");
        //JButton startRed = new JButton("Add Red");
        JButton buttonStop = new JButton("Stop");
        buttonStart.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                int blue_ball_count = 1200;

                for (int i = 0; i < blue_ball_count; i++) {
                    Ball blue_b = new Ball(canvas);
                    blue_b.setColor(Color.blue);
                    canvas.add(blue_b);

                    BallThread blue_thread = new BallThread(blue_b, BLUE_PRIORITY);
                    blue_thread.start();
                    System.out.println("Thread name = " +
                            blue_thread.getName());
                }

                Ball red_b = new Ball(canvas);
                red_b.setColor(Color.red);
                canvas.add(red_b);

                BallThread red_thread = new BallThread(red_b, RED_PRIORITY);
                red_thread.start();
                System.err.println(" RED Thread name = " +
                        red_thread.getName());
            }
        });

//        startRed.addActionListener(new ActionListener() {
//
//            @Override
//            public void actionPerformed(ActionEvent e) {
//
//                Ball b = new Ball(canvas);
//                b.setColor(Color.red);
//                canvas.add(b);
//
//                BallThread thread = new BallThread(b, RED_PRIORITY);
//                thread.start();
//                System.err.println(" RED Thread name = " +
//                        thread.getName());
//            }
//        });

        buttonStop.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

                System.exit(0);
            }
        });
        buttonPanel.add(buttonStart);
        buttonPanel.add(buttonStop);

        content.add(buttonPanel, BorderLayout.SOUTH);


    }

}

