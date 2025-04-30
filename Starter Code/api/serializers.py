from rest_framework import serializers
from .models import Product, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id',
                    'name',
                    'description', 
                    'price', 
                    'stock'
                )
    
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be greater than 0")
        return value

class OrderItemSerializer(serializers.ModelSerializer):
    # product = ProductSerializer()
    
    # if you want to flatten the product field you can use the following line instead:
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2)

    class Meta:
        model = OrderItem
        fields = ('product_name', 'product_price', 'quantity', 'item_subtotal')
        # fields = ('product', 'quantity')
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name = 'get_total_price')
    
    def get_total_price(self, obj):
        # total = 0
        # for item in obj.items.all():
        #     total += item.item_subtotal
            
        # return total
        
        # simpler way to calculate total price
        return sum(item.item_subtotal for item in obj.items.all())
    
    class Meta:
        model = Order
        fields = (
                    'order_id', 
                    'created_at', 
                    'user', 
                    'status', 
                    'items',
                    'total_price'
                )
        
class ProductInfoSerializer(serializers.Serializer):
    products = ProductSerializer(many=True)
    count = serializers.IntegerField()
    max_price = serializers.FloatField()
    min_price = serializers.FloatField()
    avg_price = serializers.FloatField()
    total_price = serializers.FloatField()