package com.codejam.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.codejam.service.DataProcessing;

@RestController
public class DataController {

	@Autowired
	private DataProcessing dataProcessing;

	@CrossOrigin
	@RequestMapping(path = "/executequery", method = RequestMethod.POST, produces = "application/json")
	@ResponseBody
	public String ExecuteQuery(@RequestBody String inputJson) {
		return dataProcessing.storeSensorData(inputJson);
	}

}