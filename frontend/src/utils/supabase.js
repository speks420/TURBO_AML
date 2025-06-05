import { createClient } from '@supabase/supabase-js';

// Initialize the Supabase client
const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY;

if (!supabaseUrl || !supabaseAnonKey) {
  console.error('Supabase credentials are missing. Make sure VITE_SUPABASE_URL and VITE_SUPABASE_ANON_KEY are set in your .env file.');
}

const supabase = createClient(supabaseUrl, supabaseAnonKey);

/**
 * Get company data from Supabase
 * 
 * @param {string} regNumber - The company registration number
 * @returns {Promise} - The company data or null
 */
export const getCompanyData = async (regNumber) => {
  try {
    const { data, error } = await supabase
      .from('companies')
      .select('*')
      .eq('registration_number', regNumber)
      .single();
    
    if (error) throw error;
    
    // Merge additional_data fields into the main company object if present
    if (data && data.additional_data) {
      const additionalData = data.additional_data;
      delete data.additional_data;
      return { ...data, ...additionalData };
    }
    
    return data;
  } catch (error) {
    console.error('Error fetching company data from Supabase:', error);
    return null;
  }
};

/**
 * Save company data to Supabase
 * 
 * @param {object} companyData - The company data to save
 * @returns {Promise} - The saved data or null
 */
export const saveCompanyData = async (companyData) => {
  try {
    // Ensure required fields
    if (!companyData.registration_number || !companyData.name) {
      throw new Error('Company data must include registration_number and name');
    }
    
    // Extract fields for our table structure
    const { 
      registration_number, 
      name, 
      status, 
      address, 
      founded_date,
      ...additionalData 
    } = companyData;
    
    // Prepare data for upsert
    const upsertData = {
      registration_number,
      name,
      status,
      address,
      founded_date,
      additional_data: Object.keys(additionalData).length > 0 ? additionalData : null
    };
    
    const { data, error } = await supabase
      .from('companies')
      .upsert(upsertData)
      .select()
      .single();
    
    if (error) throw error;
    
    // Return complete data including additional fields
    if (data && data.additional_data) {
      const additionalDataFields = data.additional_data;
      delete data.additional_data;
      return { ...data, ...additionalDataFields };
    }
    
    return data;
  } catch (error) {
    console.error('Error saving company data to Supabase:', error);
    return null;
  }
};

export default supabase; 