import json

from DnaSequence import DnaSequence

def get_db():
    """read db"""
    with open('db_dna.json', 'r') as f:
        try:
            data = json.load(f)
        except:
            data = {}
            data["batch"] = {}
            data["name_to_id"] = {}
            data["dna_db"] = []
        f.close()
    return data

def write_db(data):
    """write data to db"""
    with open('db_dna.json', 'w') as f:
        json.dump(data, f)

def get_name_by_id(id):
    data=get_db()
    try:
        return data["dna_db"][int(id)-1]["name"]
    except IndexError:
       print( "seq dy id #{} not exist".format(id))

def get_id_by_name(name):
    data = get_db()
    try:
        return data["name_to_id"][name]
    except IndexError:
       print( "name #{} not exist".format(name))

def is_name_exist(name):
    data = get_db()
    try:
        data["name_to_id"][name]
        return True
    except:
        return False

def get_sequence_by_id(id):
    data = get_db()
    try:
        return data["dna_db"][int(id)-1]["sequence"]
    except IndexError:
       print( "seq #{} not exist".format(id))

def valid_name(name,string):
    """check is name exist create new name by string and return it"""
    i=1
    if is_name_exist(name):
        name = name + string + str(i)
        while is_name_exist(name):
            i += 1
            name = name[:-1] + str(i)
    return name

def parser_seq(seq):
    """given @name_seq or #id_seq and return name_seq and sequence"""
    if seq[0] == "@":
        name = seq[1:]
        id = get_id_by_name(name)
        sequence = get_sequence_by_id(id)
    elif seq[0] == "#":
        id = seq[1:]
        sequence = get_sequence_by_id(id)
        name = get_name_by_id(id)
    return name,sequence

def change_seq_by_id(id,updata_seq):
    data = get_db()
    data["dna_db"][int(id)-1]["sequence"]=updata_seq
    write_db(data)

def create(name_create, sequence_create):
    """crete new dna in our db (db_dna.json)"""
    sequence = DnaSequence(sequence_create)
    if (name_create == "seq"):
        name = name_create + str(1)
    else:
        name = name_create
    data = get_db()
    try:
        data["name_to_id"][name]
        if name[:3] == "seq":
            while data["name_to_id"][name]:
                i = int(name[3:])
                i += 1
                name = "seq" + str(i)
        else:
            print("name seq is exist")
            return
    except:
        if (len(data["dna_db"]) == 0):
            id = 1
        else:
            id = data["dna_db"][-1]["id"] + 1
        data["dna_db"].append({"sequence": str(sequence), "name": name, "id": id})
        data["name_to_id"][name] = id
        data = {"dna_db": data["dna_db"], "name_to_id": data["name_to_id"],"batch":data["batch"]}
        write_db(data)
        print("[{}] {}:{}".format(id, name, sequence))

def updete_change(arg, name, string, sequence,index):
    """update data according to given params"""
    try:
        if arg[index] == ":":
            if arg[index+1][0:2] == "@@":
                name = valid_name(name, string)
                create(name, sequence)
            elif arg[index+1][0] == "@":
                name = arg[index+1][1:]
                create(name, sequence)
    except:
        id = get_id_by_name(name)
        change_seq_by_id(id, sequence)
        print("[{}] {}:{}".format(id, name, sequence))

def delete_seq_by_name(name):
    data=get_db()
    id=int(get_id_by_name(name))-1
    sequence=data["dna_db"][id]["sequence"]
    for seq in data["dna_db"][id+1:]:
        seq["id"]=int(seq["id"])-1
        data["name_to_id"][seq["name"]]=int(seq["id"])
    data["name_to_id"].__delitem__(name)
    data["dna_db"]=data["dna_db"][:id]+data["dna_db"][id+1:]
    write_db(data)
    print("Deleted: [{}] {}: {}".format(id+1,name,sequence))

def save_seq_or_batch_in_file(name_file,seq_or_batch):
    try:
        with open(name_file, 'r') as f:
            lines=f.read().splitlines()
            lines.append(seq_or_batch)
            f.close()
        with open(name_file, 'w') as f:
            for line in lines:
                f.write(line+"\n")
    except:
        with open(name_file, 'w') as f:
            f.write(seq_or_batch)

def seq_to_find_or_count(seq):
    """given @name_seq or #id_seq and according those return sequence"""
    if(seq[0]=="#" or seq[0]=="@"):
        seq_find=parser_seq(seq)
        seq_find=seq_find[1]
    else:
        seq_find=seq
    return seq_find

def get_index_sub_seq(seq,sub_seq):
    try:
        index_find = seq.index(sub_seq)
        return index_find+1
    except:
        return "{} not exist in sequence {}".format(sub_seq, seq)

def get_count_sub_str_in_seq(seq,seq_to_count):
    count=0
    ind = get_index_sub_seq(seq, seq_to_count)
    try:
        while len(seq) > len(seq_to_count):
            seq = seq[int(ind) + len(seq_to_count)-2:]
            count += 1
            ind = get_index_sub_seq(seq, seq_to_count)
        return count
    except:
        return ind