Feature: Battery calculations assignment

   The battery calculation module is called with parameters. The
   parameters decide which calculation is made, i.e. when called
   with Uk and Rl, I will be calculated.
   
   #@wip
   Scenario Outline: Calculate UK from UB, RI and RL
      Given the battery calculation module is online and available
      When I call the battery calculation module using the following values: <UB> for Ub, <RI> for Ri and <RL> for Rl
      Then The module calculates the correct value of <UK>

      Examples: Calculate current UK as UB - (RI * (UB / (RI + RL)))
         |  UB  |  RI |  RL  | UK       |
         | 5.0  | 2.5 | 13.0 | 4.193548 |
         | 5.0  | 2.5 | 20.0 | 4.444444 |
         | 5.0  | 5.0 | 13.0 | 3.611111 |
         | 5.0  | 5.0 | 20.0 | 4.000000 |
         | 10.0 | 2.5 | 13.0 | 8.387097 |
         | 10.0 | 2.5 | 20.0 | 8.888889 |
         | 10.0 | 5.0 | 13.0 | 7.222222 |
         | 10.0 | 5.0 | 20.0 | 8.000000 |
   
   #@wip
   Scenario Outline: Calculate I from Uk and Rl
      Given the battery calculation module is online and available
      When I call the battery calculation module with <Uk> for Uk and <Rl> for Rl
      Then The module calculates the correct value of <I>

      Examples: Calculate current I as Uk / Rl
         |  Uk |  Rl |   I |
         | 0.0 | 2.5 | 0.0 |
         | 5.0 | 2.5 | 2.0 |

   #@wip
   Scenario Outline: Calculate RI from UB, UK and RL
      Given the battery calculation module is online and available
      When I call the battery calculation module using the following values: <UB> for Ub, <UK> for Uk and <RL> for Rl
      Then The module calculates the correct value of <RI>

      Examples: Calculate current RI as ( UB – UK ) / ( UK / RL )
         |  UB |  UK  |  RL  | RI    |
         | 2.0 | 5.0  | 7.0  | -4.2  |
         | 2.0 | 5.0  | 14.0 | -8.4  |
         | 2.0 | 10.0 | 7.0  | -5.6  |
         | 2.0 | 10.0 | 14.0 | -11.2 |
         | 5.0 | 5.0  | 7.0  |  0.0  |
         | 5.0 | 5.0  | 14.0 |  0.0  |
         | 5.0 | 10.0 | 13.0 | -3.5  |
         | 5.0 | 10.0 | 14.0 | -7.0  |

   #@wip
   Scenario Outline: Calculate RL from UK and I
      Given the battery calculation module is online and available
      When I call the battery calculation module with <UK> for Uk and <I> for I
      Then The module calculates the correct value of <RL>

      Examples: Calculate current RL as Uk / I
         |  UK  |  I  |  RL |
         | 5.0  | 2.0 | 2.5 |
         | 10.0 | 2.0 | 5.0 |
         | 5.0  | 5.0 | 1.0 |
         | 10.0 | 5.0 | 2.0 |