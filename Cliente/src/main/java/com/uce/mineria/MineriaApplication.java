package com.uce.mineria;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.ansi.AnsiColor;
import org.springframework.boot.ansi.AnsiOutput;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.*;

@SpringBootApplication
public class MineriaApplication {

    public static void main(String[] args) {
        ConfigurableApplicationContext context = SpringApplication.run(MineriaApplication.class, args);

        String version = context.getEnvironment().getProperty("application.version");

        System.out.println("\n\n");

        String padding = "          ";
        System.out.println(AnsiOutput.toString(AnsiColor.BRIGHT_BLUE,
                padding + ":: basaltos ::   (v" + version + ")\n"));

        System.out.println("**********************************************");
        System.out.println("      Iniciado en --> http://localhost:" + context.getEnvironment().getProperty("server.port"));
        System.out.println("**********************************************");


    }

}

