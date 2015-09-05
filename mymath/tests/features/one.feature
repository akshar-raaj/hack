Feature: Verify that correct factorial is computed

	Scenario: Verify factorial for 3
		Given I compute the factorial of 3
		Then The result is 6
