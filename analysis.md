DB Analysis :
    Products :
        Product: 
            - name 
            - sku 
            - price 
            - desc
            - tags 
            - weight 
            - flag = new , feature
        
        Brand :
            - name

        Category:
            - name
            - image


        Reviews:
            - product
            - user
            - review
            - rate
            - create_date


        Images:
            - product
            - image



    Users :
        - Profile
            - name 
            - email
            - image


        - User Phone Number
            - user
            - phone_number
            - type


        - Adress
            - user
            - adress
            - title




    Orders : 
        Orders :
            - id 
            - order_status [Recieved - Processed - Shipped - Delivered]
            - Order Time
            - Sub Total
            - Dicount
            - Delivery Fee
            - Total
            - Delivery location


        OrderDetails :
            - serial
            - order
            - product
            - price
            - quantity
