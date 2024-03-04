import re
from search_engines import google_search

# TODO:
# Grab all the h2 <span class="heading-counter"></span>
# Format it for search
# See which one misses the "- Available On: "
# Add h2 to query_list.


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def format_text_for_search(text):
    print()


""" def find_headings(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    inside_line_one = False

    for line in lines:
        # Check if the line starts with "## Hello"
        if line.startswith('## <span class="heading-counter"></span>'):
            inside_line_one = True
            hello_section = line.strip()
            print(hello_section)
            continue """

# TODO:
# Google limit is 100 request a day.
# Make it work 50 times (since 2 requests are made each time?)
# And run it for 2 days.
def find_headings(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    modified_lines = []
    inside_line_one = False
    inside_line_two = False


    line_one = '## <span class="heading-counter"></span>'
    pattern_to_remove = r'## <span class="heading-counter"></span>'
    #line_two = '- Available On:'

    regex_apple = r'https://podcasts\.apple\.com[^\s]+'
    regex_spotify = r'https://open\.spotify\.com[^\s]+'
    query_tails = [
        {"name":"Apple Podcast", "regex": regex_apple, "class":"btn-apple-podcast"},
        {"name":"Spotify", "regex": regex_spotify, "class": "btn-spotify"}
        ]
    
    list_item = "- Available On:"

    #test_count = 0
    for line in lines:
        if line.startswith(line_one): # count is temporarly: and test_count == 0
            #inside_line_one = True
            modified_lines.append(line)
            heading_section = line.strip()
            print(heading_section)
            query = remove_pattern_from_heading(pattern_to_remove, line)

            for query_tails_number in range(0, len(query_tails)):
                name = query_tails[query_tails_number]["name"]
                css_class = query_tails[query_tails_number]["class"]
                regex = query_tails[query_tails_number]["regex"]
                answer_google = google_search(query + " " + name)
                amount_of_search_results = len(answer_google["items"]) # KeyError: 'items' "Wealthtrack Podcast"
                url = None

                for search_result_count in range(0, amount_of_search_results):
                    url = answer_google["items"][search_result_count]["link"]
                    matches = re.findall(regex, url)
                    if matches:
                        a_tag = ' <a href="' + url + '" target="_blank" class="' + css_class + '">'+ name +'</a>,'
                        list_item += a_tag
                        print(a_tag)
                    print(search_result_count)

            
            if list_item.endswith(","):
                list_item.rstrip(",")

            modified_lines.append(list_item + "\n")

            #test_count+=1

    # Write the modified lines back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(modified_lines)


def remove_pattern_from_heading(pattern, heading):
    output_string = re.sub(pattern, '', heading)
    return output_string


def find_content(file_path):
    content = read_file(file_path)


def main():
    print("Running: Read Markdown")
    markdown_file_path = r"D:\Documents\GitHub\chooseinvesting\src\blog\the-ultimate-list-of-investing-podcasts.md"
    #print(read_file(markdown_file_path))
    find_headings(markdown_file_path)


if __name__ == '__main__':
    main()