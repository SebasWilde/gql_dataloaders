import graphene
from graphene_django import DjangoObjectType
from graphene_django.debug import DjangoDebug

from account.models import User

from promise import Promise
from promise.dataloader import DataLoader


class UserLoader(DataLoader):
    def batch_load_fn(self, keys):
        users = {user.id: user for user in User.objects.filter(id__in=keys)}
        return Promise.resolve([users.get(user_id) for user_id in keys])


user_loader = UserLoader()


class UserType(DjangoObjectType):
    class Meta:
        model = User

    best_friend = graphene.Field(lambda: UserType)
    best_friends = graphene.List(lambda: UserType)

    def resolve_best_friend(self, info):
        if self.best_friend_id:
            return user_loader.load(self.best_friend_id)

    def resolve_best_friends(self, info):
        if self.best_friends.exists():
            return user_loader.load_many(self.best_friends.values_list('id', flat=True))


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    debug = graphene.Field(DjangoDebug, name='_debug')
    get_user = graphene.Field(UserType)

    def resolve_get_user(self, info):
        return User.objects.first()


schema = graphene.Schema(query=Query)
