Feature: Verify num increment works properly

	Scenario: Increment once
		Given I have access to increment
		When I use increment
		Then num is 1

	Scenario: Increment twice
		Given I have access to increment
		When I use increment
		Then num is 2