# class BalanceViewset(YkGenericViewSet):
    
#     def get_queryset(self):
#         return User.objects.filter(email=self.request.user)
    
#     @swagger_auto_schema(
#         operation_summary="Transer",
#         operation_description="Transfer any amount",
#         responses={200: EmptySerializer(), 400: BadRequestResponseSerializer()},
#         request_body=BalanceSerializer(),
#     )
    
#     @action(methods=["POST"], detail=False, permission_classes=[permissions.IsAuthenticated])
    
#     def create_(self, request, *args, **kwargs):
#         transf_ser = BalanceSerializer(data=self.request.data)
#         print(transf_ser)    
           