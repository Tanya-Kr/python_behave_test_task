Feature: Test scenarios for Product page

  @cart
  Scenario: Add product to cart from product page
    Given a user visits product page "http://automationpractice.com/index.php?id_product=2&controller=product"
    When click on Add to cart button
    Then pop up with success message is displayed

#  @quantity
#  Scenario: Up product quantity
#    Given a user visits product page "http://automationpractice.com/index.php?id_product=2&controller=product"
#    When click on button to up product quantity
#    Then product quantity should be equal 2
#
#  @quantity
#  Scenario: Down product quantity
#    Given a user visits product page "http://automationpractice.com/index.php?id_product=2&controller=product"
#    When change quantity on 3
#    And click on button to down product quantity
#    Then product quantity should be equal 2
