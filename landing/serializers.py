from rest_framework import serializers

from landing.models import Heroi, Universo, Habilidade, Arg_vilao


class UniversoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universo
        fields = ('__all__')

class HabilidadeDTOSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField()

class HabilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidade
        fields = ('id', 'nome')

class HeroiSerializer(serializers.ModelSerializer):
    habilidade = HabilidadeSerializer(many=True)
    class Meta:
        model = Heroi
        fields = ('nome','fraqueza','universo', 'habilidade')


class ArgVilaoSerializer(serializers.ModelSerializer):
    hab_vilao = HabilidadeDTOSerializer(many=True)
    class Meta:
        model = Arg_vilao
        fields =('id','nome', 'hab_vilao')

