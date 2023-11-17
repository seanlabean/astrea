from glob import glob
global INCL; INCL = "./inc"
global DEST; DEST = "./site"
global NAME; NAME = "S. C. Lewis"
global DOMAIN; DOMAIN = "www.sc-lewis.com"
global LICENSE; LICENSE = "NULL"
global TABLEOFCONTENTS; TABLEOFCONTENTS = "toc"

def lexicon():
    return glob(INCL+"/*.htm")

def init_site_file(lex_f):
    fn = lex_f.split('/')[-1]
    fn = fn.split('.')[0]
    with open(DEST+'/'+fn+'.html', 'w') as f:
        return f, fn

def write_header(f, fn, head, cat_dict):
    with open(DEST+'/'+fn+'.html', 'w') as f:
        f.write("<!DOCTYPE html><html lang='en'>")
        f.write("<meta charset='utf-8'/><meta name='viewport' content='width=device-width, inital-scale=1'/><link href='../links/main.css' type='text/css' rel='stylesheet'/><link href='../media/asterix.png' type='image/png' rel='shortcut icon'/>")
        f.write("<title>" + NAME + "&mdash;" + fn + "</title></head>")
        f.write("<body>")
        f.write("<header><a href='home.html'><img src='../media/icon/henge.png' width='160' height='80'></a></header>")
        for line in head:
            f.write(line)
        # if fn == TABLEOFCONTENTS:
        #     for key in cat_dict.keys():
        #         f.write(key + " " + str(cat_dict[key]))
        f.close()
    
def write_nav(f, fn, cat_dict):
    with open(DEST+'/'+fn+'.html', 'a') as f:
        f.write("<nav>")
        f.write("<ul>")
        # find this filename as a value in the category dict. Return the category.
        match_cat = next((key for key, values in cat_dict.items() if fn in values), None)
        # make nav bar for each page. note which category the current page belongs AND mark current page in bar
        for cat, pages in cat_dict.items():
            if cat == 'no-proc': continue
            f.write("<h2>"+cat+"</h2>") if cat == match_cat else f.write("<h4>"+cat+"</h4>")
            for page in pages: f.write("<li><a href='"+page+".html' class='_self'>" + page + "</a></li>") \
                if page == fn else f.write("<li><a href='"+page+".html'>" + page + "</a></li>")
            
        f.write("</ul>")
        f.write("</nav>")
    return

def write_toc_body(cat_dict):
    with open(DEST+'/'+TABLEOFCONTENTS+'.html', 'a') as f:
        f.write("<body>")
        f.write("<main>")
        f.write("<ul>")
        for page in sorted([value for values in cat_dict.values() for value in values]):
            f.write("<li><a href='"+page+".html'>"+page+"</a></li>")
            #f.write(key + " " + str(cat_dict[key]))
        f.write("</ul>")
        f.write("</main>")
        f.close()

def parse_body(lex_f, fn, cat_dict):
    with open(lex_f) as inc:
        # SLICE out and process header lines
        inc_lines = inc.readlines()
        ind_head = [i for i, x in enumerate(inc_lines) if x == '---\n']
        if len(ind_head) == 2:
            # we have a header
            head = inc_lines[ind_head[0] + 1:ind_head[1]]
            body_lines = inc_lines[ind_head[1] + 1:]
        else:
            # no or erroneous head
            head = []
            body_lines = inc_lines
        inc.close()
    with open(DEST+'/'+fn+'.html', 'a') as f:
        write_header(f, fn, head, cat_dict)
        write_nav(f, fn, cat_dict)
        for line in body_lines:
            f.write(line) #f.write(markdown.markdown(line))
        f.close()

def write_footer(fn):
    with open(DEST+'/'+fn+'.html', 'a') as f:
        f.write("<footer><hr />")
        #fpedited(f, srcpath)
        f.write("<b>Sean C. Lewis</b> © 2023 — ")
        f.write("<a href='" + LICENSE + "' target='_blank'>BY-NC-SA 4.0</a>")
        f.write("</footer>")
        f.write("</body>")
        f.write("</html>")

def preparse_header(lex_f, fn, categories):
    with open(lex_f) as inc:
        # SLICE out and process header lines
        inc_lines = inc.readlines()
        ind_head = [i for i, x in enumerate(inc_lines) if x == '---\n']
        if len(ind_head) == 2:
            # we have a header
            head = inc_lines[ind_head[0] + 1:ind_head[1]]
            cat = [i for i, x in enumerate(head) if x.split(':')[0] == 'category']
            this_cat = head[cat[0]].split(':')[-1].strip()
            categories.setdefault(this_cat, [])
            #categories[fn] = head[cat[0]].split(':')[-1].strip()
            categories[head[cat[0]].split(':')[-1].strip()].append(fn)
        else:
            # no or erroneous head
            head = []
        inc.close()
    return categories

def write_table_of_contents(cat_dict):
    write_header(None, TABLEOFCONTENTS, [], cat_dict)
    write_toc_body(cat_dict)
    write_footer(TABLEOFCONTENTS)
    return
    
def finalize(f, fn):
    try:
        f.close()
    except:
        print(f"Error processing file {fn}")

def engine():
    lex = lexicon()
    # preprocess loop to get table of contents (which files belong to which categories)
    categories = {}
    for lex_f in lex:
        f, fn = init_site_file(lex_f)
        preparse_header(lex_f, fn, categories)
    # make table of contents
    write_table_of_contents(categories)
    # main processing loop
    for lex_f in lex:
        f, fn = init_site_file(lex_f)
        parse_body(lex_f, fn, categories)
        write_footer(fn)
        finalize(f, fn)
if __name__ == "__main__":
    engine()