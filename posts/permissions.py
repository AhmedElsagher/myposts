from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        print("request.method",request.method )
        if request.method in permissions.SAFE_METHODS:
            if obj.status=="PUBLIC":
                return True
            if request.user in obj.shared_with_users.all():
                return True
        # elif request.method =="POST":
        #     if not request.user.is_authenticated:
        #         print("obj.user", obj.user)
        #         if obj.user==None:
        #             return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
