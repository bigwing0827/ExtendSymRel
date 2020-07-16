# coding:UTF-8
import os
import csv
import json

def ReadCSV(file_name):
    list_csv = []
    rfile = os.path.abspath(file_name)
    with open(rfile, 'r') as f:
        #fieldnames = ['Word1', 'tag1', 'Word2', 'tag2']
        fieldnames = ['Word1', 'tag1', 'Word2', 'tag2', 'sim']
        reader = csv.DictReader(f, fieldnames=fieldnames)
        for row in reader:
            list_csv.append(row)
    return list_csv

def ExtractSymRel(free_word,list_SD,ext_type):
    ## Json_tag
    sr_w = ext_type + '_word' ## synonym_word or relation_word
    sr_l = ext_type + '_label' ## synonym_label or relation_label
    sr_s = ext_type + '_similarity' ## synonym_similarity or relation_similarity
    ## synonym/relation information
    new_list = []
    for entry_sd in list_SD:
        sr_word = ""
        sr_label = ""
        flag = False
        if entry_sd['Word1'] == free_word:
            sr_word = entry_sd['Word2']
            sr_label = entry_sd['tag2']
            flag = True
        if entry_sd['Word2'] == free_word:
            sr_word = entry_sd['Word1']
            sr_label = entry_sd['tag1']
            flag = True
        ## Overlap
        if len(sr_word)!=0 and len(sr_label)!=0:
            for i in range(len(new_list)):
                if sr_word == new_list[i][sr_w]:
                    flag = False
                    break
        if flag:
            new_list.append({sr_w:sr_word,sr_l:sr_label,sr_s:entry_sd['sim']})
    ## Sort (label > similarity)
    new_list = sorted(new_list, key=lambda x:(x[sr_l],x[sr_s]), reverse=True)
    return new_list

def WordInfo(f_word,sym_set,rel_set):
    ## free_word's label
    if len(sym_set)!=0:
        f_label = sym_set[0]['synonym_label']
    else:
        f_label = "Unknown"
    ## free/synonym/relation information
    one_word_info = {
        "free_word":f_word,
        "free_label":f_label,
        "synonym_list":sym_set,
        "relation_list":rel_set
    }
    return one_word_info
        
def ExtendKeyWords():
    ## SD_dictionary
    sym_name='../SD_data/synonym_rand.csv'
    rel_name='../SD_data/relation_rand.csv'
    r_list = ReadCSV(rel_name)
    s_list = ReadCSV(sym_name)
    ## free_word
    input_words = ["エミリア","音声認識","会議"]
    word_list = {'free_words':input_words}
    #input_words = request.get_json()
    #list_sfdc = {'free_words': input_words['free_words']}
    ## Search Synonym Relation
    KW_INFO = []
    for free_word in word_list['free_words']:
        s_words = ExtractSymRel(free_word,s_list,'synonym')
        r_words = ExtractSymRel(free_word,r_list,'relation')
        fsr_set = WordInfo(free_word,s_words,r_words)
        KW_INFO.append(fsr_set)
    ##
    result = {
        "search_list":KW_INFO
    }
    #return result
    return (json.dumps(result, sort_keys=False, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    output_data = ExtendKeyWords()
    print(output_data)
