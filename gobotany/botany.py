from gobotany import models

class SpeciesReader(object):

    def query_species(self,
                      scientific_name=None,
                      is_simple_key=True,
                      **kwargs):
        if scientific_name is not None:
            return models.Taxon.objects.filter(scientific_name__iexact=scientific_name,
                                               simple_key=is_simple_key)
        else:
            base_query = models.Taxon.objects
            for k, v in kwargs.items():
                base_query = base_query.filter(
                    character_values__character__short_name=k,
                    character_values__value=v)
            return base_query.filter(simple_key=is_simple_key)

    def species_images(self, species, max_rank=10,
                       image_types=None):
        query = {'rank__lte': max_rank}
        if image_types:
            if isinstance(image_types, basestring):
                image_types = [s.strip() for s in image_types.split(',')]
            query['image_type__name__in'] = image_types
        # If we have a string assume it's the scientific name, otherwise
        # we have a taxon object or id
        if isinstance(species, basestring):
            species = models.Taxon.objects.get(scientific_name__iexact=species)
        return species.images.filter(**query)

_reader = SpeciesReader()
query_species = _reader.query_species
species_images = _reader.species_images
