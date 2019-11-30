package com.codejam.application;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.web.SpringBootServletInitializer;
import org.springframework.context.annotation.ComponentScan;

@ComponentScan("com.codejam")
@SpringBootApplication
public class CodeJamDataServicesApplication extends SpringBootServletInitializer {

	public static void main(String[] args) {
		SpringApplication.run(CodeJamDataServicesApplication.class, args);
	}
}