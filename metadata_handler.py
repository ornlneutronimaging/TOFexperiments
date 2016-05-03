def isolate_metadata(commented_data):
    '''
    isolate the various metadata
    '''
    list_labels = []
    distance_source_detector = -1
    detector_offset = -1
    tmp_list_of_elements = []    
    list_of_elements = []
    
    for _comments_of_file in commented_data:
    
        for _line in _comments_of_file:

            [name, value] = _line.split(':')
            if name == '# Label':
                list_labels.append(value.strip('\n'))
            elif name == '# distance_source_detector (m)':
                if distance_source_detector == -1:
                    distance_source_detector = float(value)
            elif name == '# detector_offset (micros)':
                if detector_offset -- -1:
                    detector_offset = float(value)
            elif name == '# List of elements':
                for _element in value.strip('\n').split(','):
                    tmp_list_of_elements.append(_element)
                
    list_of_elements = set(tmp_list_of_elements)

    return (list_labels,
            distance_source_detector,
            detector_offset,
            list_of_elements)
    
