from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Разрешение для редактирования и удаления данных"""

    def has_permission(self, request, view):
        """Проверка безопасного метода либо аутентификации"""

        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        """Проверка безопасного метода либо соответствия юзера автору"""

        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
