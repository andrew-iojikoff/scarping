from search_community.search_communitys import CommunityData

if __name__ == "__main__":
    print('Введите название сообщества')
    communityName = str(input())
    Community = CommunityData(communityName)
    communities_hrefs = Community.get_communities_by_name()
    communities_data = Community.get_communities_data()
    print(communities_hrefs)

