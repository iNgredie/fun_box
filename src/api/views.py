from time import time

from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import VisitedLinksSerializer
from api.utils import redis_instance, get_domain


class VisitedLinksAPIView(APIView):
    serializer_class = VisitedLinksSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            links = serializer.validated_data['links']
            redis_instance.sadd(int(time()), *links)
            response = {
                'status': 'ok'
            }
            return Response(response, 200)


class VisitedDomainsAPIView(APIView):
    http_method_names = ['get', 'head']

    def get(self, request):
        links = []
        uniq_domains = set()
        from_ = request.GET.get('from')
        to = request.GET.get('to')
        if not from_.isdigit() or not to.isdigit():
            response = {'status': 'not valid query'}
            return Response(response, 400)

        for key in redis_instance.scan_iter():
            if (not key.decode('utf-8').isdigit()
                or int(key) < int(from_)
                    or int(key) > int(to)):
                continue
            if redis_instance.type(key).decode('utf-8') == 'set':
                links.extend(redis_instance.smembers(key))
            for link in links:
                uniq_domains.add(get_domain(link.decode('utf-8')))

        response = {
            'domains': uniq_domains,
            'status': 'ok'
        }
        return Response(response, 200)
