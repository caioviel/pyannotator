<?xml version="1.0" encoding="ISO-8859-1"?>
<!-- Generated	by NCL Eclipse -->
<ncl id="composerConnBase">

<head>

<connectorBase>
		<causalConnector id="onSelectionPauseStopStart">
					<simpleCondition role="onSelection" />
					<compoundAction operator="seq">
						<simpleAction role="pause" max="unbounded" qualifier="par" />
						<simpleAction role="stop" max="unbounded" qualifier="par" />
						<simpleAction role="start" max="unbounded" qualifier="par" />
					</compoundAction>
				</causalConnector>	


				<causalConnector id="onEndStart">
					<simpleCondition role="onEnd" />
					<simpleAction role="start" max="unbounded" qualifier="par" />
				</causalConnector>
				
				<causalConnector id="onBeginStart">
					<simpleCondition role="onBegin" />
					<simpleAction role="start" max="unbounded" qualifier="par" />
				</causalConnector>
				
				<causalConnector id="onSelectionResumeStopStart">
					<simpleCondition role="onSelection" />
					<compoundAction operator="seq">
						<simpleAction role="resume" max="unbounded" qualifier="par" />
						<simpleAction role="stop" max="unbounded" qualifier="par" />
						<simpleAction role="start" max="unbounded" qualifier="par" />
					</compoundAction>
				</causalConnector>	

				
				<causalConnector id="onSelectionAbort">
					<simpleCondition role="onSelection" />
					<simpleAction role="abort" max="unbounded" qualifier="par" />
				</causalConnector>	
				
				<causalConnector id="onSelectionSetStopStart">
					<simpleCondition role="onSelection" />
					<connectorParam name="setValue"/>
					<compoundAction operator="seq">
						<simpleAction role="set" value="$setValue" max="unbounded" qualifier="seq"/>
						<simpleAction role="stop" max="unbounded" qualifier="seq" />
						<simpleAction role="start" max="unbounded" qualifier="seq" />
					</compoundAction>
				</causalConnector>

				<causalConnector id="onSelectionSetAbortStart">
					<simpleCondition role="onSelection" />
					<connectorParam name="setValue"/>
					<compoundAction operator="seq">
						<simpleAction role="set" value="$setValue" max="unbounded" qualifier="seq"/>
						<simpleAction role="abort" max="unbounded" qualifier="seq" />
						<simpleAction role="start" max="unbounded" qualifier="seq" />
					</compoundAction>
				</causalConnector>
				
				<causalConnector id="onSelectionTestSet">
        			<connectorParam name="testValue"/>
        			<connectorParam name="setValue"/>
        			<compoundCondition operator="and">
         				<simpleCondition role="onSelection"/>
         				<assessmentStatement comparator="eq">
            				<attributeAssessment role="propertyType" eventType="attribution" attributeType="nodeProperty"/>
            				<valueAssessment value="$testValue"/>
          				</assessmentStatement>		
        			</compoundCondition>
        			<simpleAction role="set" value="$setValue" max="unbounded" qualifier="seq"/>
      			</causalConnector>
      			
      			<causalConnector id="onSelectionTestAbortStart">
        			<connectorParam name="testValue"/>
        			<compoundCondition operator="and">
         				<simpleCondition role="onSelection"/>
         				<assessmentStatement comparator="eq">
            				<attributeAssessment role="propertyType" eventType="attribution" attributeType="nodeProperty"/>
            				<valueAssessment value="$testValue"/>
          				</assessmentStatement>		
          			</compoundCondition>
          			
          			<compoundAction operator="seq">
						<simpleAction role="abort" max="unbounded" qualifier="seq" />
						<simpleAction role="start" max="unbounded" qualifier="seq" />
					</compoundAction>
      			</causalConnector>
      			
      			<causalConnector id="onBeginSet">
      				<connectorParam name="setValue"/>
      				<simpleCondition role="onBegin"/>
      				<simpleAction role="set" value="$setValue" max="unbounded" qualifier="seq"/>
			    </causalConnector>
			    
			    <causalConnector id="onSelectionTest2AbortStartSet">
        			<connectorParam name="testValue1"/>
        			<connectorParam name="testValue2"/>
        			<connectorParam name="setValue"/>
        			<compoundCondition operator="and">
         				<simpleCondition role="onSelection"/>
         				<!--compoundStatement operator="and"-->
         					<assessmentStatement comparator="eq">
            					<attributeAssessment role="propertyType1" eventType="attribution" attributeType="nodeProperty"/>
            					<valueAssessment value="$testValue1"/>
          					</assessmentStatement>		
          					<assessmentStatement comparator="eq">
            					<attributeAssessment role="propertyType2" eventType="attribution" attributeType="nodeProperty"/>
            					<valueAssessment value="$testValue2"/>
          					</assessmentStatement>     	
				         <!--/compoundStatement-->
        			</compoundCondition>
        			<compoundAction operator="seq">
        				<simpleAction role="abort" max="unbounded" qualifier="par" />
						<simpleAction role="start" max="unbounded" qualifier="par" />		
						<simpleAction role="set" value="$setValue" max="unbounded" qualifier="seq"/>
			        </compoundAction>
      			</causalConnector>
      			
      			<causalConnector id="onEndStop">
      				<simpleCondition role="onEnd" />
					<simpleAction role="stop" max="unbounded" qualifier="par" />
			   </causalConnector>
			   
			   
			   <causalConnector id="onEndAttributionTest2StopStart">
        			<connectorParam name="testValue1"/>
        			<connectorParam name="testValue2"/>
					<compoundCondition operator="and">
						<simpleCondition role="onEndAttribution"/>
						
						<!--compoundStatement operator="and"-->
	         				<assessmentStatement comparator="eq">
            					<attributeAssessment role="propertyType1" eventType="attribution" attributeType="nodeProperty"/>
            					<valueAssessment value="$testValue1"/>
          					</assessmentStatement>		
          					<assessmentStatement comparator="eq">
            					<attributeAssessment role="propertyType2" eventType="attribution" attributeType="nodeProperty"/>
            					<valueAssessment value="$testValue2"/>
          					</assessmentStatement>   
          				<!--/compoundStatement-->
					</compoundCondition>
					<compoundAction operator="seq">
						<simpleAction role="stop" max="unbounded" qualifier="par"/>
						<simpleAction role="start" max="unbounded" qualifier="par" />
					</compoundAction>
			</causalConnector>
			
				<causalConnector id="onEndAttributionTestStart">
					<connectorParam name="testValue"/>
					<compoundCondition operator="and">
						<simpleCondition role="onEndAttribution"/>
							<assessmentStatement comparator="eq">
								<attributeAssessment role="propertyType" eventType="attribution" attributeType="nodeProperty"/>
								<valueAssessment value="$testValue"/>
							</assessmentStatement>
					</compoundCondition>
					<simpleAction role="start" max="unbounded" qualifier="par"/>
			</causalConnector>


				<causalConnector id="onEndAttributionTest2Start">
				<connectorParam name="testValue1"/>
        			<connectorParam name="testValue2"/>
					<compoundCondition operator="and">
						<simpleCondition role="onEndAttribution"/>
						
						<!--compoundStatement operator="and"-->
	         				<assessmentStatement comparator="eq">
            					<attributeAssessment role="propertyType1" eventType="attribution" attributeType="nodeProperty"/>
            					<valueAssessment value="$testValue1"/>
          					</assessmentStatement>		
          					<assessmentStatement comparator="eq">
            					<attributeAssessment role="propertyType2" eventType="attribution" attributeType="nodeProperty"/>
            					<valueAssessment value="$testValue2"/>
          					</assessmentStatement>   
          				<!--/compoundStatement-->
					</compoundCondition>
					<simpleAction role="start" max="unbounded" qualifier="par"/>
			</causalConnector>


			<causalConnector id="onEndAttributionNETestStop">
					<connectorParam name="testValue"/>
					<compoundCondition operator="and">
						<simpleCondition role="onEndAttribution"/>
							<assessmentStatement comparator="ne">
								<attributeAssessment role="propertyType" eventType="attribution" attributeType="nodeProperty"/>
								<valueAssessment value="$testValue"/>
							</assessmentStatement>
					</compoundCondition>
					<simpleAction role="stop" max="unbounded" qualifier="par"/>
			</causalConnector>
			
			<causalConnector id="onEndAttributionTestStop">
					<connectorParam name="value"/>
					<compoundCondition operator="and">
						<simpleCondition role="onEndAttribution"/>
							<assessmentStatement comparator="eq">
								<attributeAssessment role="test" eventType="attribution" attributeType="nodeProperty"/>
								<valueAssessment value="$value"/>
							</assessmentStatement>
					</compoundCondition>
					<simpleAction role="stop" max="unbounded" qualifier="par"/>
			</causalConnector>

		<causalConnector id="onSelectionTestSetAbort">
        		<connectorParam name="testValue"/>
			<connectorParam name="setValue"/>
        		<compoundCondition operator="and">
         			<simpleCondition role="onSelection"/>
         			<assessmentStatement comparator="eq">
            			<attributeAssessment role="propertyType" eventType="attribution" attributeType="nodeProperty"/>
            				<valueAssessment value="$testValue"/>
          			</assessmentStatement>		
          		</compoundCondition>
			<compoundAction operator="seq">
				<simpleAction role="set" value="$setValue" max="unbounded" qualifier="seq"/>
				<simpleAction role="abort" max="unbounded" qualifier="seq" />
			</compoundAction>
      		</causalConnector>

		<causalConnector id="onEndSetAbort">
			<connectorParam name="setValue"/>
         		<simpleCondition role="onEnd"/>
			<compoundAction operator="seq">
				<simpleAction role="set" value="$setValue" max="unbounded" qualifier="seq"/>
				<simpleAction role="abort" max="unbounded" qualifier="seq" />
			</compoundAction>
      		</causalConnector>

		<causalConnector id="onAbortTestStart">
        		<connectorParam name="testValue"/>
			<connectorParam name="setValue"/>
        		<compoundCondition operator="and">
         			<simpleCondition role="onAbort"/>
         			<assessmentStatement comparator="eq">
            			<attributeAssessment role="propertyType" eventType="attribution" attributeType="nodeProperty"/>
            				<valueAssessment value="$testValue"/>
          			</assessmentStatement>		
          		</compoundCondition>
			<simpleAction role="start" max="unbounded" qualifier="seq" />
      		</causalConnector>


		<causalConnector id="onBeginPauseStopStart">
			<simpleCondition role="onBegin" />
			<compoundAction operator="seq">
				<simpleAction role="pause" max="unbounded" qualifier="par" />
				<simpleAction role="stop" max="unbounded" qualifier="par" />
				<simpleAction role="start" max="unbounded" qualifier="par" />
			</compoundAction>
		</causalConnector>

		<causalConnector id="onSelectionSetAbort">
			<connectorParam name="setValue"/>
         		<simpleCondition role="onSelection"/>
			<compoundAction operator="seq">
				<simpleAction role="set" value="$setValue" max="unbounded" qualifier="seq"/>
				<simpleAction role="abort" max="unbounded" qualifier="seq" />
			</compoundAction>
      		</causalConnector>
      		

      		
      		<causalConnector id="onKeySelectionSetStop">
      				<connectorParam name="theKey"/>
					<simpleCondition role="onSelection" key="$theKey"/>
					<connectorParam name="setValue"/>
					<compoundAction operator="seq">
						<simpleAction role="set" value="$setValue" max="unbounded" qualifier="seq"/>
						<simpleAction role="stop" max="unbounded" qualifier="seq" />
					</compoundAction>
			</causalConnector>
			
			
			<causalConnector id="onBeginTestStart">
        			<connectorParam name="testValue"/>
        			<compoundCondition operator="and">
         				<simpleCondition role="onBegin"/>
         				<assessmentStatement comparator="eq">
            				<attributeAssessment role="propertyType" eventType="attribution" attributeType="nodeProperty"/>
            				<valueAssessment value="$testValue"/>
          				</assessmentStatement>		
        			</compoundCondition>
        			<simpleAction role="start" max="unbounded" qualifier="par"/>
      			</causalConnector>
</connectorBase>

</head>

</ncl>

