import clips

class ClipsEngine():
    def __init__(self):
        self._clips = clips.Environment()

    def _add_facts(self,facts):
        for fact in facts:
            self._clips.assert_string(fact)

    def _reload_clp(self,file):
        self._clips.load(file)

    def _get_facts(self):
        return self._clips.facts()

    def _get_hit_rule(self):
        return self._clips.activations()

    def _run(self):
        self._clips.run()

    def _detect(self,shape):
        self._clips.run()

        is_shape_same = False

        for fact in self._clips.facts():
            if (str(fact) == shape):
                is_shape_same = True
        
        return is_shape_same