from rest_framework import serializers
from .models import Music, Artist, Comment

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id',)


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name',)


class ArtistDetailSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(many=True)
    
    class Meta(ArtistSerializer.Meta):
        fields = ArtistSerializer.Meta.fields + ('music_set',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # fields = __all__
        # music으로 하면 music_id를 다른 key로 입력해야한다.
        fields = ('id', 'content','music_id',)


class MusicDetailSerializer(serializers.ModelSerializer):
    # related names를 설정할 시 source를 설정해주면된다.
    # comments = CommentSerializer(source='comment_set', many=True)
    comment_set = CommentSerializer(many=True)
    
    class Meta(MusicSerializer):
        fields = MusicSerializer.Meta.fields + ('comment_set',)

