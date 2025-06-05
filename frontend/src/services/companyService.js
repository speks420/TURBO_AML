import api from './api';
import { getCompanyData as getSupabaseCompanyData, saveCompanyData as saveSupabaseCompanyData } from '../utils/supabase';

/**
 * Search for companies
 * 
 * @param {string} query - The search query
 * @param {number} limit - Maximum number of results to return
 * @param {number} offset - Offset for pagination
 * @returns {Promise} - The search results
 */
export const searchCompanies = async (query, limit = 10, offset = 0) => {
  try {
    const response = await api.get('/api/search', {
      params: { q: query, limit, offset }
    });
    return response.data;
  } catch (error) {
    console.error('Error searching companies:', error);
    throw error;
  }
};

/**
 * Get company details by registration number
 * 
 * @param {string} regNumber - The company registration number
 * @returns {Promise} - The company details
 */
export const getCompanyDetails = async (regNumber) => {
  try {
    // First try to get from backend API
    const response = await api.get(`/api/company/${regNumber}`);
    const apiData = response.data;
    
    // Then try to get supplementary data from Supabase
    const supabaseData = await getSupabaseCompanyData(regNumber);
    
    // If we have supplementary data, merge it with the API data
    if (supabaseData) {
      // Merge while giving precedence to API data for common fields
      return {
        ...supabaseData,
        ...apiData,
        // Ensure registry_data is preserved
        registry_data: apiData.registry_data
      };
    }
    
    return apiData;
  } catch (error) {
    console.error('Error getting company details:', error);
    throw error;
  }
};

/**
 * Save supplementary company data
 * 
 * @param {object} companyData - The company data to save
 * @returns {Promise} - The saved data
 */
export const saveCompanyData = async (companyData) => {
  try {
    return await saveSupabaseCompanyData(companyData);
  } catch (error) {
    console.error('Error saving company data:', error);
    throw error;
  }
}; 