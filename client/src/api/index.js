/* eslint-disable*/
import axios from 'axios'
import { get, post } from './http'

// =======================> 用户 API
// 登录
export const loginIn = (params) => post(`user/login/status`, params)
// 注册
export const SignUp = (params) => post(`user/add`, params)
// 更新用户信息
export const updateUserMsg = (params) => post(`user/update`, params)
// 返回指定ID的用户
export const getUserOfId = (id) => get(`user/detail?id=${id}`)
//
export const getUserAvatar = (id) => get(`user/avatar?id=${id}`)


// =======================> 歌单 API
// 获取全部歌单
export const getSongList = () => get('songList')
// 获取歌单类型
export const getSongListOfStyle = (style) => get(`songList/style/detail?style=${style}`)
// 返回标题包含文字的歌单
export const getSongListOfLikeTitle = (keywords) => get(`songList/likeTitle/detail?title=${keywords}`)
// 返回歌单里指定歌单ID的歌曲
export const getListSongOfSongId = (songListId) => get(`listSong/detail?songListId=${songListId}`)


// =======================> 歌手 API
// 返回所有歌手
export const getAllSinger = () => get('singer')
// 通过性别对歌手分类
export const getSingerOfSex = (sex) => get(`singer/sex/detail?sex=${sex}`)


// =======================> 收藏 API
// 返回的指定用户ID的收藏列表
export const getCollectionOfUser = (userId) => get(`collection/detail?userId=${userId}`)
// 添加收藏的歌曲 type: 0 代表歌曲， 1 代表歌单
export const setCollection = (params) => post(`collection/add`, params)


// =======================> 评分 API
// 提交评分
export const setRank = (params) => post(`rank/add`, params)
// 获取指定歌单的评分
export const getRankOfSongListId = (songListId) => get(`rank?songListId=${songListId}`)


// =======================> 评论 API
// 添加评论
export const setComment = (params) => post(`comment/add`, params)
// 点赞
export const setLike = (params) => post(`comment/like`, params)
// 返回所有评论
export const getAllComment = (type, id) => {
  let url = ''
  if (type === 1) {
    url = `comment/songList/detail?songListId=${id}`
  } else if (type === 0) {
    url = `comment/song/detail?songId=${id}`
  }
  return get(url)
}


// =======================> 歌曲 API
// 返回指定歌曲ID的歌曲
export const getSongOfId = (id) => get(`song/detail?id=${id}`)
// 返回指定歌手ID的歌曲
export const getSongOfSingerId = (id) => get(`song/singer/detail?singerId=${id}`)
// 返回指定歌手名的歌曲
export const getSongOfSingerName = (keywords) => get(`song/singerName/detail?name=${keywords}`)
// 下载音乐
export const download = (url) => axios({
  method: 'get',
  url: url,
  responseType: 'blob'
})


//======================>讨论贴API
//返回所有帖子
export const getAllTopics = () =>  get('topics')

//根据类型返回对应帖子
export const getTopicOfType = (type) => get(`topics/type?type=${type}`)

//增加点击量
export const updateClickNum = (id) => post(`topics/updateClick?id=${id}`)

//查询用户发表的文章总数
export const countTopic = (id) => get(`topics/countTopic?id=${id}`)

//查询某一用户发表的所有文章
export const getUserTopics = (id) => get(`topics/getUserTopics?id=${id}`)

//上传文章
export const uploadTopic = (params) => post(`topics/uploadTopic`,params)

//根据文章ID获得发表文章对象的头像
// export const getUserAvatar = (id) => get(`topics/getUserAvatar?id=${id}`)


// ==========================================>bv获取API
export const  getVideoBv = (bv) => get(`getBv?bv=${bv}`)
export const  getVideoDm = (bv) => get(`getDm?bv=${bv}`)

