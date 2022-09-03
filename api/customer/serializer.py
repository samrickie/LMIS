from rest_framework import serializers

from customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'age']

# class CustomerSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     age = serializers.IntegerField()

    # def create(self, validated_data):
    #     """creates and returns an instace ofthe customer"""
    #     return Customer.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """update and return an existing customer"""
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.age = validated_data.get('age', instance.age)
    #     instance.save()
    #     return instance
