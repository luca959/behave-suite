Feature:Security Testing XSS
  Scenario Outline: the <Pages> isn't resilient to XSS
    Given the application page, "<Pages>"
     When an attacker tries to input the malicious <attack>
     Then the application will return an alert with the "xss" string
  Examples: Similar Pages
    | Pages         | attack |
    | echo-attr.php | ?name='> <script>alert('xss')</script> <!--'|
    | echo-attr2.php | ?name="> <script>alert('xss')</script> <!--"|
    | echo-name-protected.php | ?name='> <script>alert('xss')</script> <!--'|
    | echo.php | ?name='> <script>alert('xss')</script> <!--' |
    | echo-name.php| ?name="<script>alert('xss')</script>" |

  Scenario Outline: the <Pages> isn't resilient to XSS
    Given the application page, "<Pages>"
     When an attacker tries to input the malicious <attack>
     Then the application will return an alert with the "1" string
  Examples: Similar Pages
    | Pages | attack |
    | img-loader-protected.php | ?target=' onerror=alert(1) <!--|
    | img-loader-protected2.php | ?target=' onerror=alert(1) <!-- |
    | img-loader.php | ?target=' onerror=alert(1) <!--|

  Scenario Outline: the <Pages> isn't resilient to XSS
    Given the application page, "<Pages>"
     When an attacker tries to input the malicious <attack>
     Then the application will return a clickable link and an alert will appear with the "1" string
  Examples: Similar Pages
    | Pages | attack |
    | redirect.php | ?target=javascript:alert(1)|
    | redirect_protected.php | ?target=javascript:alert(1) |
