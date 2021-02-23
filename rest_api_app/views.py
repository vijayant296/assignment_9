from django.shortcuts import render, HttpResponse
from django.views.generic import View
from rest_api_app.models import Techie
from django.core.serializers import serialize
import json
from .forms import TechieForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import time
import requests
from django.http import Http404


@method_decorator(csrf_exempt, name='dispatch')
class Techie_data(View):
    def get(self, request, *args, **kwargs):
        empty_list = []
        techie_info = Techie.objects.all()
        for entry in techie_info:
            empty_list.append([entry])
        if len(empty_list) < 1:
            return HttpResponse(json.dumps({'msg': 'No item found','time':time.time()}, indent=4))

        else:
            json_data = serialize('json', techie_info)
            p_data = json.loads(json_data)
            final_list = []
            for obj in p_data:
                Techie_bio = obj['fields']
                final_list.append(Techie_bio)
            json_data = json.dumps(final_list, indent=4)
            return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        data = request.body
        tech_data = json.loads(data)
        form = TechieForm(tech_data)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse(json.dumps({'msg': 'create item successfully'}))
        if form.errors:
            json_data = json.dumps(form.errors)
            return HttpResponse(json_data, content_type='application/json')


@method_decorator(csrf_exempt, name='dispatch')
class Techie_data_id(View):
    def get(self, request, id, *args, **kwargs):
        try:
            techie_info = Techie.objects.get(techie_id=id)
            print(techie_info)

            data = {
                'techie_name': techie_info.techie_name,
                'techie_skill': techie_info.techie_skill,
                'techie_profile': techie_info.techie_profile,
                'techie_salary': techie_info.techie_salary,
            }

            json_data = json.dumps(data)
        except Techie.DoesNotExist:
            # techie_info = None
            # json_data = json.dumps({'msg': 'Techie info not found'}, indent=4)
            raise Http404("Techie does not exist")
        return HttpResponse(json_data, content_type='application/json')


@method_decorator(csrf_exempt, name='dispatch')
class Techie_update_id(View):
    def get_object_by_id(self, id):
        try:
            techie_info = Techie.objects.get(techie_id=id)
        except Techie.DoesNotExist:
            techie_info = None
        return techie_info

    def put(self, request, id, *args, **kwargs):
        techie = self.get_object_by_id(id)

        if techie is None:
            json_data = json.dumps({'msg': 'No match found during updation'})
            return HttpResponse(json_data)

        data = request.body
        provided_data = json.loads(data)
        original_data = {

            'techie_name': techie.techie_name,
            'techie_skill': techie.techie_salary,
            'techie_profile': techie.techie_profile,
            'techie_salary': techie.techie_salary,
        }

        original_data.update(provided_data)
        # for k,v in provided_data.items():
        #     original_data[k]=v
        form = TechieForm(original_data, instance=techie)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'message updated successfully'})
            return HttpResponse(json_data, content_type='application/json')
        if form.errors:
            json_data = json.dumps(form.errors)
            return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, id, *args, **kwargs):
        techie = self.get_object_by_id(id)

        if techie is None:
            json_data = json.dumps({'msg': 'No match found to delete'})
            return HttpResponse(json_data, status=404)

        status, deleted_item = techie.delete()

        if status == 1:
            json_data = json.dumps({'msg': 'Record get deleted permanently'})
            return HttpResponse(json_data, status=404)

        json_data = json.dumps({'msg': 'Something went wrong,try again'})
        return HttpResponse(json_data, status=404)
