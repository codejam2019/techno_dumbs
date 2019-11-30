package com.codejam.service;

import java.io.File;
import java.io.PrintWriter;
import java.util.Map;
import java.util.UUID;

import org.json.JSONObject;
import org.springframework.stereotype.Component;

@Component
public class DataProcessing {

	public String storeSensorData(String inputJson) {
		String jsonFileName = generateString();
		JSONObject obj = new JSONObject(inputJson);
		String cityName = "City=" + obj.getString("City") + "\\";
		String SendorId = "SendorId=" + obj.getString("Sensor_Location") + "\\";
		String Date = "Date=" + obj.getString("Timestamp") + "\\";
		String FilePath = System.getProperty("user.dir")+"\\SensorDataDump\\" + cityName + SendorId.replaceAll(" ","") + Date.replaceAll(" ","") + jsonFileName + ".json";
		File f = new File(FilePath);
		f.getParentFile().mkdirs();
		try (PrintWriter out = new PrintWriter(f.getAbsolutePath())) {
			out.println(inputJson);
			System.out.println("Success");
			return "Success";
		} catch (Exception e) {
			System.out.println(e);
			return "Fail";
		}

	}

	public static String generateString() {
		return UUID.randomUUID().toString().replaceAll("-", "");

	}

}