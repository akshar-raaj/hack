Feature: Verify correct factorial is computed

	Scenario Outline: Verify factorial for following numbers
		Given I have the number <number>
		When I compute the factorial
		Then I see the result <result>

		Examples:
		|number | result |
		| 0     | 1      |
		| 1     | 1      |
	    | 3     | 6      |
